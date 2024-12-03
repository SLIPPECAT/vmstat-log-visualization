# VMStat Log Visualization

Easily visualize the output of **vmstat logs** with this tool.  
Analyze and understand system performance metrics like memory, CPU usage, and I/O operations in a structured and graphical format.

## Features

- Parse **vmstat log files** and extract key system performance metrics.
- Visualize data using interactive and clear charts for better analysis.
- Support for multiple datasets for comparison.

## Example Log Format

Here is an example of a **vmstat log** input:  

```
Free Memory (KB)          200000     6000000     500000.00
Cache Memory (KB)         1200000    16000000    15000000.00
Blocks In (blocks/s)      5          300000      40000.00
Blocks Out (blocks/s)     10         90000       30000.00
Context Switches          10         40000       20000.00
User CPU (%)              10         90          50.00
System CPU (%)            5          35          20.00
Idle CPU (%)              2          95          40.00
IO Wait (%)               1          60          10.00
```

Each line includes:  
1. **Metric Name**: Describes the system resource or activity being measured (e.g., "Free Memory (KB)").
2. **Minimum Value**: The lowest observed value.
3. **Maximum Value**: The highest observed value.
4. **Average Value**: The average over the logged period.
---

## Visualizations

With this tool, you can generate graphical representations of vmstat logs.  
It just show average values.  
Example visualizations include:  
- **Memory Usage (Free & Cache)**  
- **CPU Utilization (User, System, Idle, IO Wait)**  
- **Disk I/O Performance (Blocks In & Out)**  
- **System Load (Context Switches)**
- 
---

## How to Use

1. **Input Logs**: Paste your vmstat log into the tool or upload a log file.
2. **View Charts**: Analyze the graphical representation of your data.

### & Example Output
![image](https://github.com/user-attachments/assets/b1d128d2-a2d0-4cc9-94f7-8536ff550115)
![cpu](https://github.com/user-attachments/assets/3396f403-cc8e-4059-ad55-c145866a297d)
![blocksinout](https://github.com/user-attachments/assets/bb1c0a3e-464d-4071-91b1-156685892009)
![contextswitch](https://github.com/user-attachments/assets/8bd4d129-3feb-48cf-8d6f-541e05068855)
![memory](https://github.com/user-attachments/assets/1a4cdded-06cf-4de6-b1f8-87bf60e3e35d)

---
