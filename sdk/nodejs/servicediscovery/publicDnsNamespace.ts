// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputApi from "../types/input";
import * as outputApi from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a Service Discovery Public DNS Namespace resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.servicediscovery.PublicDnsNamespace("example", {
 *     description: "example",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/service_discovery_public_dns_namespace.html.markdown.
 */
export class PublicDnsNamespace extends pulumi.CustomResource {
    /**
     * Get an existing PublicDnsNamespace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PublicDnsNamespaceState, opts?: pulumi.CustomResourceOptions): PublicDnsNamespace {
        return new PublicDnsNamespace(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:servicediscovery/publicDnsNamespace:PublicDnsNamespace';

    /**
     * Returns true if the given object is an instance of PublicDnsNamespace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PublicDnsNamespace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PublicDnsNamespace.__pulumiType;
    }

    /**
     * The ARN that Amazon Route 53 assigns to the namespace when you create it.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The description that you specify for the namespace when you create it.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
     */
    public /*out*/ readonly hostedZone!: pulumi.Output<string>;
    /**
     * The name of the namespace.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a PublicDnsNamespace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PublicDnsNamespaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PublicDnsNamespaceArgs | PublicDnsNamespaceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PublicDnsNamespaceState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["hostedZone"] = state ? state.hostedZone : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as PublicDnsNamespaceArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["hostedZone"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PublicDnsNamespace.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PublicDnsNamespace resources.
 */
export interface PublicDnsNamespaceState {
    /**
     * The ARN that Amazon Route 53 assigns to the namespace when you create it.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The description that you specify for the namespace when you create it.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
     */
    readonly hostedZone?: pulumi.Input<string>;
    /**
     * The name of the namespace.
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PublicDnsNamespace resource.
 */
export interface PublicDnsNamespaceArgs {
    /**
     * The description that you specify for the namespace when you create it.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the namespace.
     */
    readonly name?: pulumi.Input<string>;
}
