import os
import time
import argparse


class Varity:
    def __init__(self, program):
        self.benchmark = program
        self.baseline = "-O3"
        self.sequence = self.get_recommended_seq()

    def get_recommended_seq(self):
        file_path = "./data/recommend_sequences.txt"
        with open(file_path, "r") as f:
            while 1:
                line = f.readline()
                if line.strip("\n") == self.benchmark:
                    return f.readline().strip("\n")

    def benchmark_specific(self):
        # Benchmark-specific compilation flags
        if self.benchmark in ["security_pgp_d", "security_pgp_e"]:
            return " -DUNIX -DPORTABLE"
        if self.benchmark == "consumer_mad":
            return " -DFPM_DEFAULT -DHAVE_CONFIG_H -DLOCALEDIR=\"/usr/local/share/locale\""
        if self.benchmark == "telecom_gsm":
            return " -DSASR -DSTUPID_COMPILER -DNeedFunctionPrototypes=1"
        if self.benchmark == "consumer_lame":
            return " -DLAMESNDFILE -DHAVEMPGLIB -DLAMEPARSE"
        return " "

    def makefile_writer(self, code_path, optimization_sequence):
        f = open(os.path.join(code_path, "Makefile"), "w")
        with open(os.path.join("./data/Makefile.llvm"), "r") as g:
            while 1:
                line = g.readline()
                if line == "":
                    break
                elif "CCC_OPTS_ADD =" in line:
                    line = line.strip("\n") + " {}\n".format(optimization_sequence)
                elif "CC_OPTS =" in line:
                    line = line.strip("\n") + self.benchmark_specific() + "\n"

                f.writelines(line)
        f.close()

    def experiment_run(self, fwrite=None):
        code_path = "./cBench_V1.1/{}/src".format(self.benchmark)
        results = {}

        for seq in [self.baseline, self.sequence]:
            # Preparing and makefile writing
            self.makefile_writer(code_path, seq)
            if os.path.exists(os.path.join(code_path, "temp.bc")):
                os.system("cd {} && sudo rm *.bc".format(code_path))
            os.system("cd {} && sudo make".format(code_path))

            # Execution program with the "__run" script and DataSet setting "1"
            # provided by cBench and record run-time.
            evaluation = "cd {} && sudo chmod +x a.out && " \
                         "(sudo ./__run 1) > ./runtime_record.txt 2>&1 && sudo rm *.bc".\
                format(code_path)
            os.system(command=evaluation)
            results[seq] = self.get_time()
            time.sleep(2)
        print("**********************************************")
        print("Application: {}, speedup: {}.\nExecution time: -O3: {} sec, "
              "MLiC: {} sec.".format(self.benchmark, round(results[self.baseline]/results[self.sequence], 2),
                                 results[self.baseline], results[self.sequence]))
        print("**********************************************")
        if fwrite != None:
            fwrite.write("%s\t%.3f\t%.3f\t%.3f\n"%(self.benchmark, results[self.baseline], results[self.sequence], round(results[self.baseline]/results[self.sequence], 2)))

    def get_time(self):
        with open("./cBench_V1.1/{}/src/runtime_record.txt".format(self.benchmark),
                  "r") as f:
            while 1:
                line = f.readline()
                if "real" in line:
                    return float(line.strip("s\n").split("m")[-1])


if __name__ == "__main__":
    apps = [
            "automotive_susan_c", "automotive_susan_e", "automotive_susan_s",
            "automotive_bitcount", "bzip2d", "office_rsynth", "telecom_gsm",
            "telecom_adpcm_c", "telecom_adpcm_d", "security_blowfish_d",
            "security_blowfish_e", "bzip2e", "telecom_CRC32", "network_dijkstra",
            "consumer_jpeg_c", "consumer_jpeg_d", "network_patricia",
            "automotive_qsort1", "security_rijndael_d", "security_rijndael_e",
            "security_sha", "office_stringsearch1", "consumer_tiff2bw",
            "consumer_tiff2rgba", "consumer_tiffdither", "consumer_tiffmedian",
            "consumer_lame", "consumer_mad", "office_ghostscript",
            "office_ispell", "security_pgp_d", "security_pgp_e"
    ]
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--app", "--application", type=str,
                            default="automotive_susan_c")
        args = parser.parse_args()
        if args.app != "ALL":
            if args.app not in apps:
                raise FileNotFoundError("Can't find {} in cBench. Check and try again, please.".
                                        format(args.app))
            var = Varity(program=args.app)
            var.experiment_run()
        else:
            fwrite = open("result.txt", "w")
            for app in apps:
                try:
                    var = Varity(program=app)
                    var.experiment_run(fwrite)
                except:
                    print("Some bugs raise while running program {}.".format(app))
                    pass

    except KeyboardInterrupt:
        os._exit(1)
