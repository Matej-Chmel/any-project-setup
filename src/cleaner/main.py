from functools import partial
from src.common.Cfg import Cfg
from src.common.fileOps import ignoreStatus, parsePatterns, purgePatterns

def main():
	cfg = Cfg.fromArgs("CLEANER", "Cleans the project of files specified in the configuration.")
	ignored = parsePatterns(cfg.get("ignore"), cfg.root)
	purgePatterns(cfg.get("purge"), partial(ignoreStatus, ignored=ignored), cfg.root)

if __name__ == "__main__":
	main()
