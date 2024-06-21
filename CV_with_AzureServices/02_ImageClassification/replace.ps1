$storageAcct = '<<Azure_storage_name>>'
(Get-Content training-images/training_labels.json) -replace '<<Azure_storage_name>>', $storageAcct | Out-File training-images/training_labels.json