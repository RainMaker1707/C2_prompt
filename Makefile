
T = $(PWD)

data: clean
	@(cd data/csv/ && zip -r $(T)/zip/data.zip *)
	@(cd labels && zip -r $(T)/zip/labels.zip *.json)
	@(cd prompt/tasks && zip -r $(T)/zip/tasks.zip *.md)

doc:
	@(cd documentation && zip -r $(T)/zip/doc.zip *.md)


clean:
	@rm -f $(T)/zip/labels.zip $(T)/zip/data.zip $(T)/zip/tasks.zip