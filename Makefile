
optimizinator: rbe picir compiler
	python optimizinator.py

.PHONY: rbe picir compiler

rbe:
	git -C rule_based_engine pull
	make -C rule_based_engine install
	cp rule_based_engine/rbe .
	cp rule_based_engine/rbe_interface.py .

picir:
	git -C PICIR pull
	cp PICIR/*.py .

compiler:
	# git -C ir_compiler pull
	cp ir_compiler/*.py .


