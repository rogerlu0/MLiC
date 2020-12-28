# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -loop-vectorize -demanded-bits -instcombine -loops -loop-simplify -inferattrs -loop-vectorize -demanded-bits -instcombine -tti -loop-accesses -barrier -correlated-propagation -loop-unswitch -basicaa -forceattrs -float2int -rpo-functionattrs -assumption-cache-tracker -early-cse -loop-unroll -lazy-value-info -block-freq -memdep -loop-rotate -loop-deletion -bdce -scoped-noalias -tbaa -gvn -mem2reg -lcssa -domtree
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
