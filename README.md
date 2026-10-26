# 🌐 Edge Node

### From Sensor Data to Local Decisions — An Interactive Edge Computing Experiment

An interactive engineering demonstration that simulates an **edge node** filtering temperature readings locally, and shows how much data is saved compared with sending everything to the cloud.

### 🌐 [Launch the Live Website](https://iamnarendren.github.io/edge-node/)

---

## 🚀 Project Overview

**Edge Node Lab** is an interactive project developed for the study of edge computing in *Introduction to Electrical Engineering*.

An edge node is a computing device placed close to where data is generated. Instead of sending every reading to a remote cloud server, it processes the data locally and forwards only what matters. In this project a laptop acts as the edge node: it filters simulated temperature readings against a 35°C threshold, measures how long this takes, and compares the amount of data with and without filtering.

## 🎯 Project Objectives

* Understand the basic architecture and purpose of an edge node.
* Implement local temperature-data processing using Python.
* Test different dataset sizes and measure execution time.
* Compare the size of the data payload with and without edge filtering.
* Present the experiment through a website that can run locally or online.
* Discuss the benefits and limitations of the experiment.

## ✨ Key Features

* **Live Experiment:** Run the edge-node filter on 10,000 to 1,000,000 simulated readings.
* **Run All Sizes:** Fill the results table with the 10,000, 100,000 and 500,000 reading tests in one click.
* **Python Program Viewer:** Read the actual `edge_node.py` source inside the website.
* **Results Table and Chart:** Execution time, alerts selected, readings filtered out, and data size with and without filtering.
* **Automatic Analysis:** Written observations generated from your own run.
* **Insights:** Key takeaways based on the measured numbers.
* **Cloud vs. Edge Comparison:** Adjust the link speed and see the estimated transfer time for both designs.
* **Dark Engineering Interface:** A dark, minimal layout inspired by modern lab dashboards.

## 🔬 Methodology

The application follows this workflow:

`Simulated Sensors → Edge Node (Filter > 35°C) → Alerts Only → Optional Cloud`

1. **Data Generation**

   Eight virtual sensors produce temperature readings chosen randomly between 20°C and 45°C. A fixed random seed makes the dataset repeatable.

2. **Local Threshold Filtering**

   Each reading is compared with the 35°C threshold. Readings above it are selected as alerts and the rest are discarded.

3. **Execution Time Measurement**

   The filtering step is timed with Python's `time.perf_counter()`.

4. **Payload Comparison**

   All readings and the alerts alone are written as JSON text to compare the data size with and without filtering.

5. **Analysis**

   Results are compared across dataset sizes to study scaling, alert rate and data saved.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Edge-node program and local web server |
| Python `http.server` | Serving the website and running experiments locally |
| HTML and CSS | Website structure and dark interface |
| JavaScript | Interface, results table, analysis and in-browser fallback |
| Canvas API | Data-size chart |
| GitHub Pages | Free online hosting |

## 🌐 Live Demonstration

**Website:** https://iamnarendren.github.io/edge-node/

Open the live website to:

1. Choose a dataset size.
2. Click **Run experiment**, or **Run all sizes**.
3. Read the results table and chart.
4. Review the analysis and insights.
5. Compare the cloud-only and edge-node designs at different link speeds.

> The hosted site runs the filtering in JavaScript inside your browser, so timings come from your own device. When run locally with `server.py`, the same experiment runs in Python.

## 📊 Experimental Results

| Readings | Execution time (s) | Alerts selected | Filtered out | Data size, all readings | Data size, alerts only | Data saved |
|---:|---:|---:|---:|---:|---:|---:|
| 10,000 | 0.000303 | 4,039 | 59.61 % | 299.0 KB | 120.8 KB | 59.61 % |
| 100,000 | 0.003620 | 40,100 | 59.90 % | 2.99 MB | 1.20 MB | 59.90 % |
| 500,000 | 0.018840 | 200,525 | 59.90 % | 14.95 MB | 6.00 MB | 59.89 % |

**What the results show**

* About 40% of readings exceeded 35°C, matching the expected rate for a 20–45°C spread.
* Filtering at the edge cut the data to be sent by about 60%.
* Processing time grew roughly in proportion to the number of readings.
* Even 500,000 readings were filtered in under 0.02 seconds.

Execution times depend on the computer and its background activity. Alert counts and data sizes stay the same in the Python version because the random seed is fixed.

## 📐 Model Scope and Limitations

* The readings are simulated; no physical temperature sensor is used.
* The experiment runs on one laptop and does not measure real network latency, energy consumption, or actual transmission time.
* Data size is the length of the readings written as JSON text, not measured network traffic.
* Cloud transfer times on the website are estimates calculated from data size and a chosen link speed.
* Real savings depend on message format, protocol overhead and whether readings are sent individually or in batches.
* The in-browser version uses a different random number generator, so its alert counts are close to, but not identical with, the Python version.

These limitations are important when interpreting the results.

## 💻 Run Locally

### Prerequisites

* Python 3 installed on your computer
* Git installed (if cloning the repository)

No extra libraries are needed; the project uses only the Python standard library.

### 1. Clone the repository

```bash
git clone https://github.com/iamnarendren/edge-node.git
cd edge-node
```

### 2. Launch the server

```bash
python server.py
```

On Mac or Linux, use `python3 server.py` if `python` is not found.

### 3. Open the website

Go to `http://localhost:8000` in your browser. The badge in the experiment section will read *engine: Python on this computer*.

Press `Ctrl + C` in the terminal to stop the server.

### Project Structure

```text
edge-node/
├── index.html     # Website (interface, results, analysis, comparison)
├── edge_node.py   # Edge-node filtering program
└── server.py      # Local web server that runs the Python experiment
```

## 🎓 Academic Information

**Project Title:** Edge Node

**Subject:** Introduction to Electrical Engineering

**Project Type:** Interactive edge-computing simulation and local data-processing demonstration

**Edge Node Lab** — Processing data where it is born.
