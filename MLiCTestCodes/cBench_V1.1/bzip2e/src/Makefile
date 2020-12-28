# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -mem2reg -alignment-from-assumptions -prune-eh -jump-threading -reassociate -scalar-evolution -functionattrs -tti -always-inline -early-cse -globaldce -strip-dead-prototypes -loop-unswitch -mem2reg -alignment-from-assumptions -prune-eh -jump-threading -reassociate -scalar-evolution -functionattrs -tti -always-inline -early-cse -globaldce -strip-dead-prototypes -loop-unswitch -sccp -domtree -loop-rotate -scoped-noalias -sjljehprepare -sancov -ipconstprop -lowerinvoke -amdgpu-annotate-kernel-features
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
