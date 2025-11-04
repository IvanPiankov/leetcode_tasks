package __Two_Sum

import (
	"reflect"
	"testing"
)

func TestTwoSumExample1(t *testing.T) {
	nums := []int{2, 7, 11, 15}
	target := 9
	expected := []int{0, 1}

	got := twoSum(nums, target)
	if !reflect.DeepEqual(got, expected) {
		t.Errorf("twoSum(%v, %d) = %v; expected %v", nums, target, got, expected)
	}
}

func TestTwoSumExample2(t *testing.T) {
	nums := []int{3, 2, 4}
	target := 6
	expected := []int{1, 2}

	got := twoSum(nums, target)
	if !reflect.DeepEqual(got, expected) {
		t.Errorf("twoSum(%v, %d) = %v; expected %v", nums, target, got, expected)
	}
}

func TestTwoSumExample3(t *testing.T) {
	nums := []int{3, 3}
	target := 6
	expected := []int{0, 1}

	got := twoSum(nums, target)
	if !reflect.DeepEqual(got, expected) {
		t.Errorf("twoSum(%v, %d) = %v; want %v", nums, target, got, expected)
	}
}
