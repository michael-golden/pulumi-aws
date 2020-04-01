// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafRegional
{
    /// <summary>
    /// Provides a WAF Regional Byte Match Set Resource for use with Application Load Balancer.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_byte_match_set.html.markdown.
    /// </summary>
    public partial class ByteMatchSet : Pulumi.CustomResource
    {
        /// <summary>
        /// Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        /// </summary>
        [Output("byteMatchTuples")]
        public Output<ImmutableArray<Outputs.ByteMatchSetByteMatchTuples>> ByteMatchTuples { get; private set; } = null!;

        /// <summary>
        /// The name or description of the ByteMatchSet.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ByteMatchSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ByteMatchSet(string name, ByteMatchSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:wafregional/byteMatchSet:ByteMatchSet", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private ByteMatchSet(string name, Input<string> id, ByteMatchSetState? state = null, CustomResourceOptions? options = null)
            : base("aws:wafregional/byteMatchSet:ByteMatchSet", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ByteMatchSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ByteMatchSet Get(string name, Input<string> id, ByteMatchSetState? state = null, CustomResourceOptions? options = null)
        {
            return new ByteMatchSet(name, id, state, options);
        }
    }

    public sealed class ByteMatchSetArgs : Pulumi.ResourceArgs
    {
        [Input("byteMatchTuples")]
        private InputList<Inputs.ByteMatchSetByteMatchTuplesArgs>? _byteMatchTuples;

        /// <summary>
        /// Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        /// </summary>
        public InputList<Inputs.ByteMatchSetByteMatchTuplesArgs> ByteMatchTuples
        {
            get => _byteMatchTuples ?? (_byteMatchTuples = new InputList<Inputs.ByteMatchSetByteMatchTuplesArgs>());
            set => _byteMatchTuples = value;
        }

        /// <summary>
        /// The name or description of the ByteMatchSet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ByteMatchSetArgs()
        {
        }
    }

    public sealed class ByteMatchSetState : Pulumi.ResourceArgs
    {
        [Input("byteMatchTuples")]
        private InputList<Inputs.ByteMatchSetByteMatchTuplesGetArgs>? _byteMatchTuples;

        /// <summary>
        /// Settings for the ByteMatchSet, such as the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests. ByteMatchTuple documented below.
        /// </summary>
        public InputList<Inputs.ByteMatchSetByteMatchTuplesGetArgs> ByteMatchTuples
        {
            get => _byteMatchTuples ?? (_byteMatchTuples = new InputList<Inputs.ByteMatchSetByteMatchTuplesGetArgs>());
            set => _byteMatchTuples = value;
        }

        /// <summary>
        /// The name or description of the ByteMatchSet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ByteMatchSetState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ByteMatchSetByteMatchTuplesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Settings for the ByteMatchTuple. FieldToMatch documented below.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<ByteMatchSetByteMatchTuplesFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// Within the portion of a web request that you want to search.
        /// </summary>
        [Input("positionalConstraint", required: true)]
        public Input<string> PositionalConstraint { get; set; } = null!;

        /// <summary>
        /// The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.
        /// </summary>
        [Input("targetString")]
        public Input<string>? TargetString { get; set; }

        /// <summary>
        /// The formatting way for web request.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public ByteMatchSetByteMatchTuplesArgs()
        {
        }
    }

    public sealed class ByteMatchSetByteMatchTuplesFieldToMatchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ByteMatchSetByteMatchTuplesFieldToMatchArgs()
        {
        }
    }

    public sealed class ByteMatchSetByteMatchTuplesFieldToMatchGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ByteMatchSetByteMatchTuplesFieldToMatchGetArgs()
        {
        }
    }

    public sealed class ByteMatchSetByteMatchTuplesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Settings for the ByteMatchTuple. FieldToMatch documented below.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<ByteMatchSetByteMatchTuplesFieldToMatchGetArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// Within the portion of a web request that you want to search.
        /// </summary>
        [Input("positionalConstraint", required: true)]
        public Input<string> PositionalConstraint { get; set; } = null!;

        /// <summary>
        /// The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.
        /// </summary>
        [Input("targetString")]
        public Input<string>? TargetString { get; set; }

        /// <summary>
        /// The formatting way for web request.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public ByteMatchSetByteMatchTuplesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ByteMatchSetByteMatchTuples
    {
        /// <summary>
        /// Settings for the ByteMatchTuple. FieldToMatch documented below.
        /// </summary>
        public readonly ByteMatchSetByteMatchTuplesFieldToMatch FieldToMatch;
        /// <summary>
        /// Within the portion of a web request that you want to search.
        /// </summary>
        public readonly string PositionalConstraint;
        /// <summary>
        /// The value that you want AWS WAF to search for. The maximum length of the value is 50 bytes.
        /// </summary>
        public readonly string? TargetString;
        /// <summary>
        /// The formatting way for web request.
        /// </summary>
        public readonly string TextTransformation;

        [OutputConstructor]
        private ByteMatchSetByteMatchTuples(
            ByteMatchSetByteMatchTuplesFieldToMatch fieldToMatch,
            string positionalConstraint,
            string? targetString,
            string textTransformation)
        {
            FieldToMatch = fieldToMatch;
            PositionalConstraint = positionalConstraint;
            TargetString = targetString;
            TextTransformation = textTransformation;
        }
    }

    [OutputType]
    public sealed class ByteMatchSetByteMatchTuplesFieldToMatch
    {
        /// <summary>
        /// When the value of Type is HEADER, enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer. If the value of Type is any other value, omit Data.
        /// </summary>
        public readonly string? Data;
        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private ByteMatchSetByteMatchTuplesFieldToMatch(
            string? data,
            string type)
        {
            Data = data;
            Type = type;
        }
    }
    }
}
