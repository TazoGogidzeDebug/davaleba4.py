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


# მაგალითი
if __name__ == "__main__":
    logger = Logger()
    logger.debug("დამატებულია debug დონე")
    logger.info("ეს არის info დონე")
    logger.warn("გაფრთხილება: warn დონე")
    logger.error("შეცდომა: error დონე")
    logger.fatal("კრიტიკული შეცდომა: fatal დონე")
