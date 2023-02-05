package stack

type Node struct {
	value interface{}
	prev  *Node
}

type Stack struct {
	head   *Node
	Length int
}

func (s *Stack) Peek() interface{} {
	if s.Length == 0 {
		return nil
	}

	return s.head.value
}

func (s *Stack) Push(value interface{}) {
	newNode := &Node{value: value, prev: s.head}
	s.head = newNode
	s.Length++
}

func (s *Stack) Pop() interface{} {
	if s.Length == 0 {
		return nil
	}

	val := s.head.value
	s.head = s.head.prev
	s.Length--

	return val
}

func NewStack() *Stack {
	return &Stack{}
}
