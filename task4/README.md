## Context
In a production setting, assume the input must scale significantly, with larger JSON files and a much
higher number of companies.
Add a short, clearly identified section in your README (or similar documentation) describing two concrete
changes you would make to your code to handle this increased scale without modifying the underlying
infrastructure (for example, changes to how the input file is read or processed)

## Current approach
the current approach uses `json.load()` which reads the entire file into memory as a Python dictionary. For files larger than 500 this can lead to excessive memory usage.

## Scaling for larger datasets

### 1. Split data into chunks
Replace `json.load` with a streaming JSON parser like [`ijson`](https://pypi.org/project/ijson/). 
This library allows iterating over the JSON structure incrementally, processing objects one by one without holding the whole file in memory.

### 2. Efficient Serialization Formats
Convert JSON files (if possible) to a columnar format like Parquet or Avro before processing. These formats are compressed, and allow selective column reads.