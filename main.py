# Databricks notebook source
import my_package

# COMMAND ----------

my_package.math.squared

# COMMAND ----------

import my_package.math

# COMMAND ----------

from my_package.math import squared

# COMMAND ----------

# MAGIC %run ./my_package/math 

# COMMAND ----------

squared(4)

# COMMAND ----------

from my_package import strings

# COMMAND ----------

strings.concatenate("foo", "bar")

# COMMAND ----------


