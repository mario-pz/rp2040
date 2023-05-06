DEST_PATH = /media/$(USER)/CIRCUITPY/

install-traffic:
	echo "copying traffic-light project"
	cp -r ./traffic-light/code.py $(DEST_PATH)

install-buttons-sample:
	echo "copying buttons-sample project"
	cp -r ./buttons-sample/code.py $(DEST_PATH)
