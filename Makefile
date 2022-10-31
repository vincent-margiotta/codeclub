TAG:=$(shell basename $(PWD))
build:
	docker build --tag $(TAG) $(PWD)
shell:
	docker run -it --hostname $(TAG) --name $(TAG) --volume $(PWD):/usr/src --rm $(TAG) bash
