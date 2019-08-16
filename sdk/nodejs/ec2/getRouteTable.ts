// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * `aws.ec2.RouteTable` provides details about a specific Route Table.
 * 
 * This resource can prove useful when a module accepts a Subnet id as
 * an input variable and needs to, for example, add a route in
 * the Route Table.
 * 
 * ## Example Usage
 * 
 * The following example shows how one might accept a Route Table id as a variable
 * and use this data source to obtain the data necessary to create a route.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const config = new pulumi.Config();
 * const subnetId = config.require("subnetId");
 * 
 * const selected = aws.ec2.getRouteTable({
 *     subnetId: subnetId,
 * });
 * const route = new aws.ec2.Route("route", {
 *     destinationCidrBlock: "10.0.1.0/22",
 *     routeTableId: selected.id,
 *     vpcPeeringConnectionId: "pcx-45ff3dc1",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_table.html.markdown.
 */
export function getRouteTable(args?: GetRouteTableArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteTableResult> & GetRouteTableResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetRouteTableResult> = pulumi.runtime.invoke("aws:ec2/getRouteTable:getRouteTable", {
        "filters": args.filters,
        "routeTableId": args.routeTableId,
        "subnetId": args.subnetId,
        "tags": args.tags,
        "vpcId": args.vpcId,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getRouteTable.
 */
export interface GetRouteTableArgs {
    /**
     * Custom filter block as described below.
     */
    readonly filters?: inputs.ec2.GetRouteTableFilter[];
    /**
     * The id of the specific Route Table to retrieve.
     */
    readonly routeTableId?: string;
    /**
     * The id of a Subnet which is connected to the Route Table (not be exported if not given in parameter).
     */
    readonly subnetId?: string;
    /**
     * A mapping of tags, each pair of which must exactly match
     * a pair on the desired Route Table.
     */
    readonly tags?: {[key: string]: any};
    /**
     * The id of the VPC that the desired Route Table belongs to.
     */
    readonly vpcId?: string;
}

/**
 * A collection of values returned by getRouteTable.
 */
export interface GetRouteTableResult {
    readonly associations: outputs.ec2.GetRouteTableAssociation[];
    readonly filters?: outputs.ec2.GetRouteTableFilter[];
    /**
     * The ID of the AWS account that owns the route table
     */
    readonly ownerId: string;
    /**
     * The Route Table ID.
     */
    readonly routeTableId: string;
    readonly routes: outputs.ec2.GetRouteTableRoute[];
    /**
     * The Subnet ID.
     */
    readonly subnetId: string;
    readonly tags: {[key: string]: any};
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
