package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"path/filepath"
	"strconv"
	"strings"
)

const deviceFile = "/sys/bus/w1/devices/28*/w1_slave"

func readTempRaw() ([]byte, error) {
	files, err := filepath.Glob(deviceFile)
	if err != nil {
		return nil, err
	}
	if len(files) == 0 {
		return nil, errors.New("no temperature sensors found")
	}
	return ioutil.ReadFile(files[0])
}

func readTemp() (float64, float64, error) {
	lines, err := readTempRaw()
	if err != nil {
		return 0, 0, err
	}

	tempLine := strings.Split(string(lines), "\n")[1]
	tempData := strings.Split(tempLine, " ")[9]
	temp, err := strconv.ParseFloat(tempData[2:], 64)
	if err != nil {
		return 0, 0, err
	}

	tempC := temp / 1000.0
	tempF := tempC*9.0/5.0 + 32.0
	return tempC, tempF, nil
}

func temperatureHandler(w http.ResponseWriter, r *http.Request) {
	tempC, tempF, err := readTemp()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Fprintf(w, "{\"celsius\": %.2f, \"fahrenheit\": %.2f}", tempC, tempF)
}

func main() {
	http.HandleFunc("/temperature", temperatureHandler)
	log.Fatal(http.ListenAndServe(":5000", nil))
}
