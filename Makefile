
T = $(PWD)

data: clean
	@(cd converted-data/csv/ && zip -r $(T)/zip/data.zip *)
	@(cd labels && zip -r $(T)/zip/labels.zip *.json)
	@(cd prompt/tasks && zip -r $(T)/zip/tasks.zip *.md)


clean:
	@rm -f zip/labels.zip zip/data.zip zip/tasks.zip