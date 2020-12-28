# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -loop-deletion -correlated-propagation -domtree -basiccg -early-cse -loop-rotate -assumption-cache-tracker -gvn -sccp -branch-prob -adce -jump-threading -targetlibinfo -constmerge -loop-simplify -alignment-from-assumptions -globals-aa -mldst-motion -dse -reassociate -licm -globalopt -memcpyopt -basicaa -prune-eh -loop-idiom -verify -tailcallelim -ipsccp -forceattrs -instcombine -indvars -bdce -strip-dead-prototypes -always-inline -functionattrs -block-freq -rpo-functionattrs -elim-avail-extern -loop-accesses -simplifycfg -loop-unswitch -loop-unroll -barrier -tti -deadargelim -memdep -inline -argpromotion -sroa -globaldce -lower-expect -demanded-bits -aa -alignment-from-assumptions -globals-aa -mldst-motion -dse -reassociate -licm -globalopt -memcpyopt -basicaa -prune-eh -loop-idiom -verify -tailcallelim -ipsccp -forceattrs -instcombine -indvars -bdce -strip-dead-prototypes -always-inline -functionattrs -block-freq -rpo-functionattrs -elim-avail-extern -loop-accesses -simplifycfg -loop-unswitch -loop-unroll -barrier -tti -deadargelim -memdep -inline -argpromotion -sroa -globaldce -lower-expect -demanded-bits -aa
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
