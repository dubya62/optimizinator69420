
optimizinator: rbe picir compiler
	python optimizinator.py

rbe:
	git -C pyrbe pull
	cp pyrbe/*.py .

picir:
	git -C PICIR pull
	cp PICIR/*.py .

compiler:
	git -C ir_compiler pull
	cp ir_compiler/*.py .

