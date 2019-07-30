
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#ifdef WIN32
#include <win32/win32_compat.h>
#pragma comment(lib, "ws2_32.lib")
WSADATA wsaData;
#endif

#ifdef HAVE_POLL_H
#include <poll.h>
#endif

#ifdef HAVE_NETINET_IN_H
#include <netinet/in.h>
#endif


#ifdef HAVE_UNISTD_H
#include <unistd.h>
#endif


#ifdef HAVE_SYS_TIME_H
#include <sys/time.h>
#endif

#ifdef HAVE_NET_IF_H
#include <net/if.h>
#endif

#ifdef HAVE_NETDB_H
#include <netdb.h>
#endif

#ifdef HAVE_SYS_IOCTL_H
#include <sys/ioctl.h>
#endif

#ifdef HAVE_SYS_SOCKET_H
#include <sys/socket.h>
#endif
#include <sys/stat.h>
#include <fcntl.h>
//
//
//
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <inttypes.h>
//
#include "nfsc/libnfs.h"
#include "nfsc/libnfs-raw.h"
#include "nfsc/libnfs-zdr.h"


int main(int argc, char *argv[])
{
	rpc_context *Rpc = rpc_init_context();
	if (!Rpc) {
		printf("failed to init context\n");
		exit(1);
        }
	rpc_destroy_context(Rpc);
	return 0;
}
