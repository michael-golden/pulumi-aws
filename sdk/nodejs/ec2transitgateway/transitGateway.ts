// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

import {ARN} from "../index";

/**
 * Manages an EC2 Transit Gateway.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.ec2transitgateway.TransitGateway("example", {
 *     description: "example",
 * });
 * ```
 */
export class TransitGateway extends pulumi.CustomResource {
    /**
     * Get an existing TransitGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TransitGatewayState, opts?: pulumi.CustomResourceOptions): TransitGateway {
        return new TransitGateway(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<TransitGatewayResult> {
        return ctx.list({...args, type: 'aws:ec2transitgateway/transitGateway:TransitGateway'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:ec2transitgateway/transitGateway:TransitGateway',
        });
    }
    /**
     * Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.
     */
    public readonly amazonSideAsn: pulumi.Output<number | undefined>;
    /**
     * EC2 Transit Gateway Amazon Resource Name (ARN)
     */
    public /*out*/ readonly arn: pulumi.Output<ARN>;
    /**
     * Identifier of the default association route table
     */
    public /*out*/ readonly associationDefaultRouteTableId: pulumi.Output<string>;
    /**
     * Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.
     */
    public readonly autoAcceptSharedAttachments: pulumi.Output<string | undefined>;
    /**
     * Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    public readonly defaultRouteTableAssociation: pulumi.Output<string | undefined>;
    /**
     * Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    public readonly defaultRouteTablePropagation: pulumi.Output<string | undefined>;
    /**
     * Description of the EC2 Transit Gateway.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    public readonly dnsSupport: pulumi.Output<string | undefined>;
    /**
     * Identifier of the AWS account that owns the EC2 Transit Gateway
     */
    public /*out*/ readonly ownerId: pulumi.Output<string>;
    /**
     * Identifier of the default propagation route table
     */
    public /*out*/ readonly propagationDefaultRouteTableId: pulumi.Output<string>;
    /**
     * Key-value tags for the EC2 Transit Gateway.
     */
    public readonly tags: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    public readonly vpnEcmpSupport: pulumi.Output<string | undefined>;

    /**
     * Create a TransitGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: TransitGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TransitGatewayArgs | TransitGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: TransitGatewayState = argsOrState as TransitGatewayState | undefined;
            inputs["amazonSideAsn"] = state ? state.amazonSideAsn : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["associationDefaultRouteTableId"] = state ? state.associationDefaultRouteTableId : undefined;
            inputs["autoAcceptSharedAttachments"] = state ? state.autoAcceptSharedAttachments : undefined;
            inputs["defaultRouteTableAssociation"] = state ? state.defaultRouteTableAssociation : undefined;
            inputs["defaultRouteTablePropagation"] = state ? state.defaultRouteTablePropagation : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsSupport"] = state ? state.dnsSupport : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["propagationDefaultRouteTableId"] = state ? state.propagationDefaultRouteTableId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpnEcmpSupport"] = state ? state.vpnEcmpSupport : undefined;
        } else {
            const args = argsOrState as TransitGatewayArgs | undefined;
            inputs["amazonSideAsn"] = args ? args.amazonSideAsn : undefined;
            inputs["autoAcceptSharedAttachments"] = args ? args.autoAcceptSharedAttachments : undefined;
            inputs["defaultRouteTableAssociation"] = args ? args.defaultRouteTableAssociation : undefined;
            inputs["defaultRouteTablePropagation"] = args ? args.defaultRouteTablePropagation : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsSupport"] = args ? args.dnsSupport : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpnEcmpSupport"] = args ? args.vpnEcmpSupport : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["associationDefaultRouteTableId"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
            inputs["propagationDefaultRouteTableId"] = undefined /*out*/;
        }
        super("aws:ec2transitgateway/transitGateway:TransitGateway", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TransitGateway resources.
 */
export interface TransitGatewayState {
    /**
     * Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.
     */
    readonly amazonSideAsn?: pulumi.Input<number>;
    /**
     * EC2 Transit Gateway Amazon Resource Name (ARN)
     */
    readonly arn?: pulumi.Input<ARN>;
    /**
     * Identifier of the default association route table
     */
    readonly associationDefaultRouteTableId?: pulumi.Input<string>;
    /**
     * Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.
     */
    readonly autoAcceptSharedAttachments?: pulumi.Input<string>;
    /**
     * Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTableAssociation?: pulumi.Input<string>;
    /**
     * Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTablePropagation?: pulumi.Input<string>;
    /**
     * Description of the EC2 Transit Gateway.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly dnsSupport?: pulumi.Input<string>;
    /**
     * Identifier of the AWS account that owns the EC2 Transit Gateway
     */
    readonly ownerId?: pulumi.Input<string>;
    /**
     * Identifier of the default propagation route table
     */
    readonly propagationDefaultRouteTableId?: pulumi.Input<string>;
    /**
     * Key-value tags for the EC2 Transit Gateway.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly vpnEcmpSupport?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TransitGateway resource.
 */
export interface TransitGatewayArgs {
    /**
     * Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.
     */
    readonly amazonSideAsn?: pulumi.Input<number>;
    /**
     * Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.
     */
    readonly autoAcceptSharedAttachments?: pulumi.Input<string>;
    /**
     * Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTableAssociation?: pulumi.Input<string>;
    /**
     * Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTablePropagation?: pulumi.Input<string>;
    /**
     * Description of the EC2 Transit Gateway.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly dnsSupport?: pulumi.Input<string>;
    /**
     * Key-value tags for the EC2 Transit Gateway.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly vpnEcmpSupport?: pulumi.Input<string>;
}

/**
 * The live TransitGateway resource.
 */
export interface TransitGatewayResult {
    /**
     * Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is `64512` to `65534` for 16-bit ASNs and `4200000000` to `4294967294` for 32-bit ASNs. Default value: `64512`.
     */
    readonly amazonSideAsn?: number;
    /**
     * EC2 Transit Gateway Amazon Resource Name (ARN)
     */
    readonly arn: ARN;
    /**
     * Identifier of the default association route table
     */
    readonly associationDefaultRouteTableId: string;
    /**
     * Whether resource attachment requests are automatically accepted. Valid values: `disable`, `enable`. Default value: `disable`.
     */
    readonly autoAcceptSharedAttachments?: string;
    /**
     * Whether resource attachments are automatically associated with the default association route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTableAssociation?: string;
    /**
     * Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly defaultRouteTablePropagation?: string;
    /**
     * Description of the EC2 Transit Gateway.
     */
    readonly description?: string;
    /**
     * Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly dnsSupport?: string;
    /**
     * Identifier of the AWS account that owns the EC2 Transit Gateway
     */
    readonly ownerId: string;
    /**
     * Identifier of the default propagation route table
     */
    readonly propagationDefaultRouteTableId: string;
    /**
     * Key-value tags for the EC2 Transit Gateway.
     */
    readonly tags?: {[key: string]: string};
    /**
     * Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.
     */
    readonly vpnEcmpSupport?: string;
}
