# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -sroa -loop-unswitch -tailcallelim -alignment-from-assumptions -reassociate -functionattrs -strip-dead-prototypes -tti -mem2reg -scalar-evolution -jump-threading -prune-eh -always-inline -early-cse -sancov -amdgpu-annotate-kernel-features -ipconstprop -sjljehprepare -lowerinvoke -external-aa -cost-model -sancov -amdgpu-annotate-kernel-features -ipconstprop -sjljehprepare -lowerinvoke -external-aa -cost-model
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
