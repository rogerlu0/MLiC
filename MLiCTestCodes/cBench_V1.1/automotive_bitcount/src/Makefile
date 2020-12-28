# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -tti -targetlibinfo -tbaa -scoped-noalias -assumption-cache-tracker -verify -simplifycfg -domtree -sroa -early-cse -lower-expect -forceattrs -inferattrs -ipsccp -globalopt -mem2reg -deadargelim -basicaa -aa -instcombine -basiccg -globals-aa -prune-eh -inline -functionattrs -argpromotion -lazy-value-info -jump-threading -correlated-propagation -tailcallelim -reassociate -loops -loop-simplify -lcssa -loop-rotate -licm -loop-unswitch -scalar-evolution -indvars -loop-idiom -loop-deletion -loop-unroll -mldst-motion -memdep -gvn -memcpyopt -sccp -demanded-bits -bdce -dse -adce -barrier -rpo-functionattrs -elim-avail-extern -float2int -branch-prob -block-freq -loop-accesses -loop-vectorize -slp-vectorizer -alignment-from-assumptions -strip-dead-prototypes -globaldce -constmerge -always-inline
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
