# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -gvn -instcombine -simplifycfg -inline -lower-expect -lazy-value-info -scalarrepl -add-discriminators -instsimplify -cfl-aa -codegenprepare -sancov -amdgpu-annotate-kernel-features -loop-distribute -ipconstprop -scalarrepl-ssa -iv-users -load-combine -instcount -alloca-hoisting -gvn -instcombine -simplifycfg -inline -lower-expect -lazy-value-info -consthoist -safe-stack -dce -cross-dso-cfi -sjljehprepare -constprop -lowerinvoke -partial-inliner -external-aa -cost-model -die -consthoist -safe-stack -dce -cross-dso-cfi -sjljehprepare -constprop -lowerinvoke -partial-inliner -external-aa -cost-model -die
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
