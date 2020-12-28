# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -sroa -dse -assumption-cache-tracker -constmerge -argpromotion -correlated-propagation -loop-vectorize -inferattrs -ipsccp -loops -mem2reg -scoped-noalias -sancov -amdgpu-annotate-kernel-features -ipconstprop -sjljehprepare -early-cse -lcssa -tailcallelim -always-inline -globalopt -aa -globals-aa -lazy-value-info -adce -sancov -amdgpu-annotate-kernel-features -ipconstprop -sjljehprepare -early-cse -lcssa -tailcallelim -always-inline -globalopt -aa -globals-aa -lazy-value-info -adce
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
