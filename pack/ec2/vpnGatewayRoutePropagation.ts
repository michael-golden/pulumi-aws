// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class VpnGatewayRoutePropagation extends lumi.NamedResource implements VpnGatewayRoutePropagationArgs {
    public readonly routeTableId: string;
    public readonly vpnGatewayId: string;

    public static get(id: lumi.ID): VpnGatewayRoutePropagation {
        return <any>undefined; // functionality provided by the runtime
    }

    public static query(q: any): VpnGatewayRoutePropagation[] {
        return <any>undefined; // functionality provided by the runtime
    }

    constructor(name: string, args: VpnGatewayRoutePropagationArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.routeTableId, "") === undefined) {
            throw new Error("Property argument 'routeTableId' is required, but was missing");
        }
        this.routeTableId = args.routeTableId;
        if (lumirt.defaultIfComputed(args.vpnGatewayId, "") === undefined) {
            throw new Error("Property argument 'vpnGatewayId' is required, but was missing");
        }
        this.vpnGatewayId = args.vpnGatewayId;
    }
}

export interface VpnGatewayRoutePropagationArgs {
    readonly routeTableId: string;
    readonly vpnGatewayId: string;
}
