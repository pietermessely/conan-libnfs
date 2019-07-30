#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class Libsmb2Conan(ConanFile):
    name = "libnfs"
    version = "0.0.1"
    description = "NFS client library"
    url = "https://github.com/sahlberg/libnfs"
    homepage = "https://github.com/sahlberg/libnfs"
    license = "LGPL-2.1"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    source_subfolder = "source_subfolder"
    install_subfolder = "install_subfolder"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
	"with_openssl": [True, False]
    }

    default_options = {
        "shared": False,
        "fPIC": True,
	"with_openssl": True
    }

    def source(self):
        if True: # if running from own customized version (needed due to exports renaming)
            git=tools.Git(folder="libnfs")
            git.clone("https://github.com/pietermessely/libnfs.git")
        else:
            git=tools.Git(folder="libnfs")
            git.clone("https://github.com/sahlberg/libnfs.git")
        os.rename("libnfs", self.source_subfolder)


    def configure(self):
        del self.settings.compiler.libcxx

    #def requirements(self):

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['ENABLE_TESTS'] = False
        cmake.definitions['ENABLE_DOCUMENTATION'] = False
        cmake.definitions['ENABLE_UTILS'] = False
        cmake.definitions['ENABLE_EXAMPLES'] = True
        cmake.definitions['CMAKE_INSTALL_PREFIX'] = self.install_subfolder
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        #self.copy("COPYING", dst="licenses", src=self.source_subfolder, keep_path=False)
        self.copy("*", dst="include", src=os.path.join(self.install_subfolder, "include"))
        self.copy("*.dll", dst="bin", src=os.path.join(self.install_subfolder, "bin"), keep_path=False)
        self.copy("*.dylib", dst="lib", src=os.path.join(self.install_subfolder, "lib"), keep_path=False)
        # rhel installs libraries into lib64
        # cannot use cmake install into package_folder because of lib64 issue
        for libarch in ['lib', 'lib64']:
            arch_dir = os.path.join(self.install_subfolder, libarch)
            cmake_dir_src = os.path.join(arch_dir, "cmake", "libnfs")
            cmake_dir_dst = os.path.join("lib", "cmake", "libnfs")
            pkgconfig_dir_src = os.path.join(arch_dir, "pkgconfig")
            pkgconfig_dir_dst = os.path.join("lib", "pkgconfig")

            self.copy("*.lib", dst="lib", src=arch_dir, keep_path=False)
            self.copy("*.a", dst="lib", src=arch_dir, keep_path=False)
            self.copy("*.so*", dst="lib", src=arch_dir, keep_path=False)
            self.copy("*.*", dst=cmake_dir_dst, src=cmake_dir_src)
            self.copy("*.*", dst=pkgconfig_dir_dst, src=pkgconfig_dir_src)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.compiler == "Visual Studio":
            if not self.options.shared:
                self.cpp_info.libs.append('ws2_32')
#        elif self.settings.os == "Linux":
