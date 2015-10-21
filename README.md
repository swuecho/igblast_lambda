# igblast using amazon lambda

1. upload the file to <code>fasta</code> folder
2. lambda function will be called on each file in <code>fasta</code> folder
3. the output of lambda function is in <code>fasta_igblasted</code>.

In theory the total proceesing time should be the same with the maxnium of invidual precessing time of each files,
instead of their sum, becuase all lambda function run in parallel. However, there is limit of concurrent request set by Amazon.
You can request to upgrade.
