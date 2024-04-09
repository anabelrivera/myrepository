# Databricks notebook source
pip install cookiecutter

# COMMAND ----------

pip install databricks_cli

# COMMAND ----------

import subprocess

subprocess.run(["python", "./run_pipeline.py"])

