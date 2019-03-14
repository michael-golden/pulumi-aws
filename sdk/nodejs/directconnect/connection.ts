// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides a Connection of Direct Connect.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const hoge = new aws.directconnect.Connection("hoge", {
 *     bandwidth: "1Gbps",
 *     location: "EqDC2",
 * });
 * ```
 */
export class Connection extends pulumi.CustomResource {
    /**
     * Get an existing Connection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState, opts?: pulumi.CustomResourceOptions): Connection {
        return new Connection(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<ConnectionResult> {
        return ctx.list({...args, type: 'aws:directconnect/connection:Connection'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:directconnect/connection:Connection',
        });
    }
    /**
     * The ARN of the connection.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
     */
    public readonly bandwidth: pulumi.Output<string>;
    /**
     * Boolean value representing if jumbo frames have been enabled for this connection.
     */
    public /*out*/ readonly jumboFrameCapable: pulumi.Output<boolean>;
    /**
     * The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
     */
    public readonly location: pulumi.Output<string>;
    /**
     * The name of the connection.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Connection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConnectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConnectionArgs | ConnectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ConnectionState = argsOrState as ConnectionState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["bandwidth"] = state ? state.bandwidth : undefined;
            inputs["jumboFrameCapable"] = state ? state.jumboFrameCapable : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ConnectionArgs | undefined;
            if (!args || args.bandwidth === undefined) {
                throw new Error("Missing required property 'bandwidth'");
            }
            if (!args || args.location === undefined) {
                throw new Error("Missing required property 'location'");
            }
            inputs["bandwidth"] = args ? args.bandwidth : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["jumboFrameCapable"] = undefined /*out*/;
        }
        super("aws:directconnect/connection:Connection", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Connection resources.
 */
export interface ConnectionState {
    /**
     * The ARN of the connection.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
     */
    readonly bandwidth?: pulumi.Input<string>;
    /**
     * Boolean value representing if jumbo frames have been enabled for this connection.
     */
    readonly jumboFrameCapable?: pulumi.Input<boolean>;
    /**
     * The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
     */
    readonly location?: pulumi.Input<string>;
    /**
     * The name of the connection.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Connection resource.
 */
export interface ConnectionArgs {
    /**
     * The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
     */
    readonly bandwidth: pulumi.Input<string>;
    /**
     * The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
     */
    readonly location: pulumi.Input<string>;
    /**
     * The name of the connection.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The live Connection resource.
 */
export interface ConnectionResult {
    /**
     * The ARN of the connection.
     */
    readonly arn: string;
    /**
     * The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
     */
    readonly bandwidth: string;
    /**
     * Boolean value representing if jumbo frames have been enabled for this connection.
     */
    readonly jumboFrameCapable: boolean;
    /**
     * The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
     */
    readonly location: string;
    /**
     * The name of the connection.
     */
    readonly name: string;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: {[key: string]: any};
}
