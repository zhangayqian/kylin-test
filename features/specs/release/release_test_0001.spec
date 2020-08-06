# Kylin Release Test

## Prepare project

* Create project "release_test_0001_project"

* Load table "load_table_list" from file "release_test_0001.json"

## MR enigine

* Create model with "model_desc_data" in data file "release_test_0001.json"

* Create cube with "cube_desc_data" in data file "release_test_0001.json", cube name is "release_test_0001_cube"

* Build segment from "2012-01-01 00:00:00" to "2013-01-01 00:00:00"

* Build segment from "2013-01-01 00:00:00" to "2014-01-30 00:00:00"

* Merge cube segment


## SPARK engine

* Clone cube "release_test_0001_cube" and name it "kylin_spark_cube", modify build engine to "SPARK"

* Build segment from "2012-01-01 00:00:00" to "2013-01-01 00:00:00"

* Build segment from "2013-01-01 00:00:00" to "2014-01-30 00:00:00"

* Merge cube segment


## FLINK engine

* Clone cube "release_test_0001_cube" and name it "kylin_flink_cube", modify build engine to "FLINK"

* Build segment from "2012-01-01 00:00:00" to "2013-01-01 00:00:00"

* Build segment from "2013-01-01 00:00:00" to "2014-01-30 00:00:00"

* Merge cube segment


## Query cube and pushdown

* Query SQL "" and specify "release_test_0001_cube" cube to query, compare result with ""

* Query SQL "" and specify "kylin_spark_cube" cube to query, compare result with ""

* Query SQL "" and specify "kylin_flink_cube" cube to query, compare result with ""

* Diasble all cube

* Query SQL "" and return result successful



