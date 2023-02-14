%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define oname uutils

Summary:	Cross-platform Rust rewrite of the GNU coreutils
Name:		%{oname}-coreutils
Version:	0.0.17
Release:	1
Group:		System/Base
License:	MIT
URL:		https://github.com/uutils/coreutils
Source0:	https://github.com/uutils/coreutils/archive/refs/tags/coreutils-%{version}.tar.gz
BuildRequires:	rust-packaging
BuildRequires:	rust >= 1.60

%description
A rust rewrite of GNU coreutils that
aims to be dropin compatible with
GNU coreutils and crossplatform.

%prep
%autosetup -p1 -n coreutils-%{version}

%build
PROFILE=release SELINUX_ENABLED=0 make

%install
make install \
      SELINUX_ENABLED=0 \
      DESTDIR="%{buildroot}" \
      PREFIX=%{_prefix} \
      MANDIR=/share/man/man1 \
      PROG_PREFIX=uu- \
      PROFILE=release \
      MULTICALL=y

%files
%{_bindir}/uu-*
%{_datadir}/bash-completion/completions/uu-*
%{_datadir}/fish/vendor_completions.d/uu-*.fish
%{_datadir}/zsh/site-functions/_uu-*
