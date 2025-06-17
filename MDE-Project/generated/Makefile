CC=clang-morello
CFLAGS=-march=morello+c64 -mabi=purecap -g

all: integration_process

integration_process: integration_process.c integration_process.h
	$(CC) $(CFLAGS) -o integration_process integration_process.c

run:
	proccontrol -m cheric18n -s enable ./integration_process

clean:
	rm -f integration_process