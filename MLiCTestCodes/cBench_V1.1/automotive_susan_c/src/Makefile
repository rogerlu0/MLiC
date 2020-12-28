# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -gvn -instcombine -simplifycfg -inline -globals-aa -lower-expect -early-cse -loop-unswitch -globaldce -functionattrs -jump-threading -scalar-evolution -alignment-from-assumptions -prune-eh -strip-dead-prototypes -reassociate -scalarrepl -place-backedge-safepoints-impl -scalarrepl-ssa -bool-ret-to-int -codegenprepare -load-combine -consthoist -lint -partial-inliner -dce -cross-dso-cfi -constprop -scalarizer -irce -gvn -instcombine -simplifycfg -inline -globals-aa -lower-expect
endif

# Declarations
ifeq ($(ZCC),) 
 ZCC = clang
endif
ifeq ($(CC_OPTS),)
 CC_OPTS = -emit-llvm 
endif
ifeq ($(LDCC),)
 LDCC = llvm-link
endif
ifeq ($(LD_OPTS),)
 LD_OPTS = -o a.out
endif

# Actions
all:		
	$(ZCC) $(CC_OPTS) -w -c *.c
	llvm-link *.bc > temp.bc
	opt $(CCC_OPTS_ADD) temp.bc > temp2.bc
	llvm-link $(LD_OPTS) temp2.bc

clean:
	rm -f a.out *.o *.a *.s *.i *.I *.bc
