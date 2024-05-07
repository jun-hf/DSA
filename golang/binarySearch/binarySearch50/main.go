package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

func main() {
	wd, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	visitPath := filepath.Join(wd, "anotherDir")
	err = os.Chdir(visitPath)
	if err != nil {
		panic(err)
	}
	cmd := exec.Command("echo", "run", "main.go")
	err = cmd.Run()
	fmt.Println("error:", err)
	time.Sleep(5 * time.Second)
}