%{?nodejs_find_provides_and_requires}
%global enable_mocha_tests 1
%global enable_nodeunit_tests 0
Name:                nodejs-async
Version:             1.5.2
Release:             2
Summary:             Higher-order functions and common patterns for asynchronous code
License:             MIT
URL:                 https://github.com/caolan/async/
Source0:             https://github.com/caolan/async/archive/v%{version}/async-%{version}.tar.gz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging
%if 0%{?enable_mocha_tests}
BuildRequires:       npm(mocha) npm(chai)
%endif
%if 0%{?enable_nodeunit_tests}
BuildRequires:       npm(nodeunit) npm(bluebird) npm(es6-promise) npm(native-promise-only) npm(rsvp)
%endif
%description
Async is a utility module which provides straight-forward, powerful functions
for working with asynchronous JavaScript. Although originally designed for
use with Node.js, it can also be used directly in the browser.
Async provides around 20 functions that include the usual 'functional'
suspects (map, reduce, filter, forEach…) as well as some common patterns
for asynchronous control flow (parallel, series, waterfall…). All these
functions assume you follow the Node.js convention of providing a single
callback as the last argument of your async function.

%prep
%setup -q -n async-%{version}

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/async
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/async

%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_mocha_tests}
%if %{_arch}==riscv64
%{nodejs_sitelib}/mocha/bin/mocha mocha_test -t 50000
%else
%{nodejs_sitelib}/mocha/bin/mocha mocha_test
%endif
%endif
%if 0%{?enable_nodeunit_tests}
%{nodejs_sitelib}/nodeunit/bin/nodeunit test/test-async.js
%endif

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/async

%changelog
* Sun Feb 27 2022 Yongqing Chen <chenyongqingdl@gmail.com> - 1.5.2-2
- Increase mocha_test check time for riscv64 arch

* Mon Aug 17 2020 Shaoqiang Kang <kangshaoqiang1@huawei.com> - 1.5.2-1
- Package init
