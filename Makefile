
T = $(PWD)

v3: clean
	@(cd converted-data/csv/ && zip -r $(T)/data.zip data/*)
	@zip -r $(PWD)/labels.zip labels/*
	@(cd prompt && zip -r $(T)/tasks.zip tasks/*)


clean:
	@rm -f labels.zip data.zip