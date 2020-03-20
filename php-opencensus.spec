#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-opencensus
Version  : 0.2.2
Release  : 5
URL      : https://pecl.php.net//get/opencensus-0.2.2.tgz
Source0  : https://pecl.php.net//get/opencensus-0.2.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: php-opencensus-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# OpenCensus PHP Extension (Alpha)
[OpenCensus](https://opencensus.io/) is a free, open-source distributed tracing
implementation based on the [Dapper Paper](https://research.google.com/pubs/pub36356.html).
This extension allows you to "watch" class method and function calls in order to
automatically collect nested spans (timing data).

%package lib
Summary: lib components for the php-opencensus package.
Group: Libraries

%description lib
lib components for the php-opencensus package.


%prep
%setup -q -n opencensus-0.2.2
cd %{_builddir}/opencensus-0.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/opencensus.so
