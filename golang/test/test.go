package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int, 20)
	ch2 := make(chan int, 20)
	done := make(chan struct{})

	go func(ch1, ch2 chan int, done chan struct{}) {
		for {
			select {
			case v, more := <-ch1:
				fmt.Println("read from ch1:", v, more)

			case v, more := <-ch2:
				fmt.Println("read from ch2:", v, more)

			case <-done:
				fmt.Println("done, starting fanout")
				close(ch1)
				close(ch2)
				fanOut(ch1)
				fanOut(ch2)

				return
			}
			time.Sleep(time.Millisecond * 100)
		}
	}(ch1, ch2, done)

	// sync.Mutex
	// sync.atomic -> atomic.Add, Load, Swap, CompareAndSwap

	sendMessage(ch1)
	sendMessage(ch2)

	close(done)

	time.Sleep(2 * time.Second)
}

func fanOut(ch <-chan int) {
	for val := range ch {
		fmt.Println(val)
	}
}

func sendMessage(ch chan<- int) {
	for i := 0; i < 20; i++ {
		ch <- i
	}
}
