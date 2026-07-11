%global tl_name tamefloats
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.42
Release:	%{tl_revision}.1
Summary:	Experimentally use \holdinginserts with LaTeX floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tamefloats
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tamefloats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tamefloats.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX's figures, tables, and \marginpars are dangerous for footnotes
(and probably also \enlargethispage). Here is a proposal (a 'patch'
package) to help, by using \holdinginserts in a simple way. It replaces
the original problem with a new one -- it is an experiment to find out
whether the new problem is less bad (or it is just a contribution to the
discussion, maybe just a summary of previous work). The files provide
further information.

