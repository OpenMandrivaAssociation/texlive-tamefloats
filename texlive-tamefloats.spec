Name:		texlive-tamefloats
Version:	0.42
Release:	3
Summary:	Experimentally use \holdinginserts with LaTeX floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tamefloats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamefloats.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamefloats.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX's figures, tables, and \marginpars are dangerous for
footnotes (and probably also \enlargethispage). Here is a
proposal (a 'patch' package) to help, by using \holdinginserts
in a simple way. It replaces the original problem with a new
one -- it is an experiment to find out whether the new problem
is less bad (or it is just a contribution to the discussion,
maybe just a summary of previous work). The files provide
further information.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tamefloats/tameflts.sty
%doc %{_texmfdistdir}/doc/latex/tamefloats/README.txt
%doc %{_texmfdistdir}/doc/latex/tamefloats/deml3541.tex
%doc %{_texmfdistdir}/doc/latex/tamefloats/fltfltdk.tex
%doc %{_texmfdistdir}/doc/latex/tamefloats/newbug.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
