PACKAGE_NAME=simpleNavigator
VERSION=1.0
BUILD_DIR=build
DESTDIR=$(BUILD_DIR)/usr/local
LIB_DIR=$(DESTDIR)/lib/simpleNavigator
BIN_DIR=$(DESTDIR)/bin
SHARE_DIR=$(DESTDIR)/share/simpleNavigator
DEBIAN_DIR=$(BUILD_DIR)/DEBIAN

all: clean build package

build:
	cd cpp && make

	mkdir -p $(LIB_DIR) $(BIN_DIR) $(SHARE_DIR)

	cp lib/libstack.so $(LIB_DIR)
	cp lib/libqueue.so $(LIB_DIR)
	cp lib/liblist.so $(LIB_DIR)

	cp -r python/ $(SHARE_DIR)
	cp -r s21_graph_algorithms/ $(SHARE_DIR)
	cp main.py $(SHARE_DIR)

	cp simpleNavigator $(BIN_DIR)
	chmod +x $(BIN_DIR)/simpleNavigator

package: $(DEBIAN_DIR)
	dpkg-deb --build $(BUILD_DIR) $(PACKAGE_NAME)_$(VERSION).deb

$(DEBIAN_DIR):
	mkdir -p $(DEBIAN_DIR)
	cp -r debian/* $(DEBIAN_DIR)

	chmod 0644 $(DEBIAN_DIR)/control

	if [ -f $(DEBIAN_DIR)/postinst ]; then chmod 0755 $(DEBIAN_DIR)/postinst; fi
	if [ -f $(DEBIAN_DIR)/prerm ]; then chmod 0755 $(DEBIAN_DIR)/prerm; fi
	if [ -f $(DEBIAN_DIR)/postrm ]; then chmod 0755 $(DEBIAN_DIR)/postrm; fi


clean:
	cd cpp && make clean
	rm -rf $(BUILD_DIR)
	rm -f *.deb
