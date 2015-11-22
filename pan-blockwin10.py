hosts = [ "a-0001.a-msedge.net", "a-0002.a-msedge.net", "a-0003.a-msedge.net", 
	"a-0004.a-msedge.net", "a-0005.a-msedge.net", "a-0006.a-msedge.net", 
	"a-0007.a-msedge.net", "a-0008.a-msedge.net", "a-0009.a-msedge.net", 
	"a-msedge.net", "a.ads1.msn.com", "a.ads2.msads.net", "a.ads2.msn.com", 
	"a.rad.msn.com", "a1621.g.akamai.net", "a1856.g2.akamai.net", 
	"a1961.g.akamai.net", "a248.e.akamai.net", "a978.i6g1.akamai.net", 
	"ac3.msn.com", "ad.doubleclick.net", "adnexus.net", "adnxs.com", 
	"ads.msn.com", "ads1.msads.net", "ads1.msn.com", "aidps.atdmt.com", 
	"aka-cdn-ns.adtech.de", "any.edge.bing.com", "apps.skype.com", 
	"az361816.vo.msecnd.net", "az512334.vo.msecnd.net", "b.ads1.msn.com", 
	"b.ads2.msads.net", "b.rad.msn.com", "bingads.microsoft.com", 
	"bs.serving-sys.com", "c.atdmt.com", "c.msn.com", "cdn.atdmt.com", 
	"cds26.ams9.msecn.net", "choice.microsoft.com", 
	"choice.microsoft.com.nsatc.net", "compatexchange.cloudapp.net", 
	"corp.sts.microsoft.com", "corpext.msitadfs.glbdns2.microsoft.com", 
	"cs1.wpc.v0cdn.net", "db3aqu.atdmt.com", "df.telemetry.microsoft.com", 
	"diagnostics.support.microsoft.com", "e2835.dspb.akamaiedge.net", 
	"e7341.g.akamaiedge.net", "e7502.ce.akamaiedge.net", 
	"e8218.ce.akamaiedge.net", "ec.atdmt.com", "feedback.microsoft-hohm.com", 
	"feedback.search.microsoft.com", "feedback.windows.com", "flex.msn.com", 
	"g.msn.com", "h1.msn.com", "h2.msn.com", "hostedocsp.globalsign.com", 
	"i1.services.social.microsoft.com", "i1.services.social.microsoft.com.nsatc.net", 
	"ipv6.msftncsi.com", "ipv6.msftncsi.com.edgesuite.net", "lb1.www.ms.akadns.net", 
	"live.rads.msn.com", "m.adnxs.com", "m.hotmail.com", "msedge.net", "msftncsi.com", 
	"msnbot-65-55-108-23.search.msn.com", "msntest.serving-sys.com", 
	"oca.telemetry.microsoft.com", "oca.telemetry.microsoft.com.nsatc.net", 
	"onesettings-db5.metron.live.nsatc.net", "pre.footprintpredict.com", 
	"preview.msn.com", "pricelist.skype.com", "rad.live.com", "rad.msn.com", 
	"redir.metaservices.microsoft.com", "reports.wes.df.telemetry.microsoft.com", 
	"s.gateway.messenger.live.com", "secure.adnxs.com", "secure.flashtalking.com", 
	"services.wes.df.telemetry.microsoft.com", "settings-sandbox.data.microsoft.com", 
	"settings-win.data.microsoft.com", "sls.update.microsoft.com.akadns.net", 
	"sO.2mdn.net", "sqm.df.telemetry.microsoft.com", "sqm.telemetry.microsoft.com", 
	"sqm.telemetry.microsoft.com.nsatc.net", "static.2mdn.net", 
	"statsfe1.ws.microsoft.com", "statsfe2.ws.microsoft.com", 
	"survey.watson.microsoft.com", "telecommand.telemetry.microsoft.com", 
	"telecommand.telemetry.microsoft.com.nsatc.net", "telemetry.appex.bing.net", 
	"telemetry.microsoft.com", "telemetry.urs.microsoft.com", "ui.skype.com", 
	"view.atdmt.com", "vortex-bn2.metron.live.com.nsatc.net", 
	"vortex-cy2.metron.live.com.nsatc.net", "vortex-sandbox.data.microsoft.com", 
	"vortex-win.data.microsoft.com", "vortex.data.microsoft.com", "watson.live.com", 
	"watson.microsoft.com", "watson.ppe.telemetry.microsoft.com", 
	"watson.telemetry.microsoft.com", "watson.telemetry.microsoft.com.nsatc.net", 
	"wes.df.telemetry.microsoft.com", "win10.ipv6.microsoft.com", 
	"www.bingads.microsoft.com", "www.go.microsoft.akadns.net" ]

print "set tag win10-tracker comments \"Windows 10 Tracking Host\""

for host in hosts:
	print "set address %s fqdn %s" % (host, host)
	print "set address %s tag win10-tracker" % (host)


print "set address-group \"Win10 Trackers\" dynamic filter \"win10-tracker\""
