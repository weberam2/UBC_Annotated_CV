import csv
import math
import requests

filename = "altmetvalues.tex"


def get_altmetric_data(doi):
    url = f"https://api.altmetric.com/v1/doi/{doi}"
    response = requests.get(url)
    if response.status_code == 200:  # | response2.status_code == 200:
        data = response.json()
        score = math.floor(data.get("score") or 0)
        readers = data.get("readers_count") or 0
        posts = data.get("cited_by_posts_count") or 0
        news = data.get("cited_by_msm_count") or 0
        # policy = data.get("cited_by_policy_count") or 0
        pct = data.get("context", {}).get("all", {}).get("pct") or 0
        threemonthpct = (
            data.get("context", {}).get("similar_age_3m", {}).get("pct") or 0
        )
        wiki = data.get("cited_by_wikipedia_count") or 0

        altmet = ""
        altmet += f"Altmetric score = {score}"

        if int(pct) > 0:
            altmet += (
                f"; $>$ {pct}\\% all altmetric papers; "
                f"$>$ {threemonthpct}\\% last three months"
            )

        altmet += (
            f". {readers} user saves, "
            f"{posts} social-media posts, "
            f"{news} news outlets, "
            f"and {wiki} English Wikipedia pages."
        )
        return altmet
    else:
        return "No Altmetric data to report."


latex_alt = []
dois_to_altmet = {
    "10.1038/nn.2657": "\\ntypecalalt",
    "10.1038/nn0809-957a": "\\pdlimalt",
    "10.1615/VisualizImageProcComputatBiomed.2013006007": "\\warsialt",
    "10.9778/cmajo.20120020": "\\anglinalt",
    "10.1016/j.pscychresns.2014.02.004": "\\psychotropicalt",
    "10.1016/j.pnpbp.2014.04.001": "\\psychopharmalt",
    "10.1007/s10334-013-0420-5": "\\ethanolalt",
    "10.3389/fneur.2018.00575": "\\pathologicalalt",
    "10.3174/ajnr.A6114": "\\punctatealt",
    "10.1002/nbm.4222": "\\rtwostaralt",
    "10.3174/ajnr.A7086 ": "\\perinatalalt",
    "10.3389/fphys.2021.809943": "\\campbellfractalalt",
    "10.1002/hbm.25801": "\\campbellreviewalt",
    "10.1016/j.neuroimage.2022.119702": "\\bartelalt",
    "10.1002/jmri.28448": "\\fothergillalt",
    "10.46292/sci23-00068": "\\scialt",
    "10.3389/fnhum.2024.1316117": "\\dcdchangesalt",
    "10.3389/fnhum.2024.1276057": "\\dcdcontrolsalt",
    "10.3390/nu16152559": "\\ironalt",
    "10.1371/journal.pcsy.0000024": "\\sickkidsalt",
    "10.1093/cercor/bhae426": "\\dhcpalt",
    "10.1038/s41390-025-03966-6": "\\carmichaelalt",
    "10.1002/nbm.70065": "\\zhucmroalt",
    "10.1101/2025.03.28.645973": "\\sochanpreprintalt",
    "10.1101/2023.12.08.570818": "\\dhcppreprintalt",
    "10.1101/2022.06.28.22276567": "\\scipreprintalt",
    "10.55458/neurolibre.00029": "\\mrishinyalt",
    "10.1016/j.nic.2017.09.005": "\\myelinchapteralt",
}


def get_unpaywall_data(doi, oa_count):
    url = f"https://api.unpaywall.org/v2/{doi}?email=unpaywall_01@example.com"
    response = requests.get(url)
    if response.status_code == 200:  # | response2.status_code == 200:
        data = response.json()
        if data.get("is_oa") is True:
            oa_count += 1
            return oa_count

    return oa_count


oa_count = 0
for key in dois_to_altmet:
    # print(key)
    # get_altmetric_data(key)
    latex_alt.append(
        f"\\newcommand{{{dois_to_altmet[key]}}}{{{get_altmetric_data(key)}}}"
    )
    oa_count = get_unpaywall_data(key, oa_count)


latex_alt.append(f"\\newcommand{{\\oacount}}{{{oa_count}}}")

with open(filename, "w") as file:
    file.write("\n".join(latex_alt))
