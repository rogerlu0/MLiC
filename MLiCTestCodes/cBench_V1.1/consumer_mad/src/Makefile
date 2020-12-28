# ************ CCC - passing optimization flags ************ 
ifeq ($(CCC_OPTS),)
 CCC_OPTS =  -I. -DFPM_DEFAULT -DHAVE_CONFIG_H -DLOCALEDIR="/usr/local/share/locale"
endif
ifeq ($(CCC_OPTS_ADD),)
 CCC_OPTS_ADD =  -memcpyopt -loop-rotate -instcombine -loop-simplify -loop-unswitch -adce -slp-vectorizer -tailcallelim -memcpyopt -loop-rotate -instcombine -loop-simplify -memcpyopt
endif

# Declarations
ifeq ($(ZCC),) 
 ZCC = clang
endif
ifeq ($(CC_OPTS),)
 CC_OPTS = -emit-llvm -I. -DFPM_DEFAULT -DHAVE_CONFIG_H -DLOCALEDIR="/usr/local/share/locale"
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
