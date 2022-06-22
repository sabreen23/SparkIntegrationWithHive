import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
SparkContext.setSystemProperty("hive.metastore.uris", "thrift://sandbox-hdp.hortonworks.com:9083")
sparkSession = (SparkSession.builder.appName('integration-pyspark-hive').enableHiveSupport().getOrCreate())
sparkSession.sql('show databases').show()
AirlineDF= sparkSession.read.option("header","true").csv("airlines1.csv")
sparkSession.sql("create database flights").show()
sparkSession.sql("use flights").show()
AirlineDF1=AirlineDF.select("Year","Reporting_Airline")
AirlineDF1.write.saveAsTable("flights.air")



