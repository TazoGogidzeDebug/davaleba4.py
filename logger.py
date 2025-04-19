class Logger:
    def log(self, level, message):
        print(f"[{level}] {message}")

    def debug(self, message):
        self.log("DEBUG", message)

    def info(self, message):
        self.log("INFO", message)

    def warn(self, message):
        self.log("WARN", message)

    def error(self, message):
        self.log("ERROR", message)

    def fatal(self, message):
        self.log("FATAL", message)


if __name__ == "__main__":
    logger = Logger()
    logger.debug("debug დონე")
    logger.info("info დონე")
    logger.warn("warn დონე")
    logger.error("error დონე")
    logger.fatal("fatal დონე")
