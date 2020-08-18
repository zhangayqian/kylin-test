# kylin-test
Automated test code warehouse based on [gauge](https://docs.gauge.org/?os=macos&language=python&ide=vscode) for [Apache Kylin](https://github.com/apache/kylin).

### IDE
Gauge support IntelliJ IDEA and VSCode as development IDE.
However, IDEA cannot detect the step implementation method of Python language, just support java.
VSCode is recommended as the development IDE.

### Clone repo
```
git clone https://github.com/zhangayqian/kylin-test
```

### Prepare environment
 * Install python3 compiler and version 3.6 recommended
 * Install gauge
 ```
 brew install gauge
 ```
 If you encounter the below error:
 ```
 Download failed: https://homebrew.bintray.com/bottles/gauge- 1.1.1.mojave.bottle.1.tar.gz
 ```
 You can try to download the compressed package manually, put it in the downloads directory of homebrew cache directory, and execute the installation command of gauge again.

* Install required dependencies
```
pip install -r requirements.txt
```

## Directory structure
* features/specs: Directory of specification file.
  A specification is a business test case which describes a particular feature of the application that needs testing. Gauge specifications support a .spec or .md file format and these specifications are written in a syntax similar to Markdown.
  
* features/step_impl: Directory of Step implementations methods.
  Every step implementation has an equivalent code as per the language plugin used while installing Gauge. The code is run when the steps inside a spec are executed. The code must have the same number of parameters as mentioned in the step.
  Steps can be implemented in different ways such as simple step, step with table, step alias, and enum data type used as step parameters.

* data: Directory of data files needed to execute test cases. Such as cube_desc.json.

* env/default: Gauge configuration file directory.

* kylin_instance: Kylin instance configuration file directory.

* kylin_utils: Tools method directory.

## Run Gauge specifications
* Run all specification
```
gauge run
```
* Please refer to https://docs.gauge.org/execution.html?os=macos&language=python&ide=vscode learn more.

