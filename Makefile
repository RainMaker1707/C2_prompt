
T = $(PWD)

v3: clean
	@(cd converted-data/csv/ && zip -r $(T)/data.zip ./*)
	@zip -r $(PWD)/labels.zip labels/*


clean:
	@rm labels.zip data.zip