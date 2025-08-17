# datascienceproject

# end to end  data science project

### workflow--ML Pipeline

1. Data Ingestion
# inputs like data from various sources (databases, APIs, etc.)
2. Data Validation
# we check the quality and integrity of the data, looking for missing values, outliers, and inconsistencies. we check schema of input data we getting
3. Data Transformation
4. Model Training
5. Model Evaluation
6. Model Deployment

## workflows
1. update config.yaml
# data ingestion related information we update in config.yaml
2. update schema.yaml
# data validation related information we update in schema.yaml, whenever we get new test data to test our model that schema needs to be validated
3. update params.yaml
# model training related information we update in params.yaml, where we specify the hyperparameters and other settings for training the model
4. update the entity
5. update the configuration manager in src config 
# this is a class that manages the configuration of the project, including loading and validating configuration files
# updated in 1_data_ingestion.ipynb
6. update the components
7. update the pipeline
# we need to create two types of pipelines training and batch prediction
# we create a pipeline that orchestrates the entire workflow, connecting the components and ensuring data flows through the system correctly
# we define the sequence of steps and how data will be passed between them
# we also need to update the pipeline configuration to reflect any changes in the components or their interactions
# we need to ensure that the pipeline is flexible and can accommodate new components or changes to existing ones
# we may need to update the pipeline code to handle new data sources or processing steps
# we also need to update the pipeline tests to ensure that everything is working correctly
8. update the main.py