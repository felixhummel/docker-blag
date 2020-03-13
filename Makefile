locally:
	# pull existing layers
	docker pull registry.gitlab.com/felixhummel/blag-build:master
	docker build \
		-t registry.gitlab.com/felixhummel/blag-build:master \
		.
